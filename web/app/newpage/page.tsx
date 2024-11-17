import { useAppContext } from '@/context/app-context'
export default function NewPage() {
    const { mutateUserProfile, userProfile, apps } = useAppContext()

    return(

        <div className='flex px-3 py-1'>
            <p>userProfile.name</p>
            <p>userProfile.email</p>
        </div>
    )
}
